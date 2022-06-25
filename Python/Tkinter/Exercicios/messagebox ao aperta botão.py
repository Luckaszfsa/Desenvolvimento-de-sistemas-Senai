from tkinter import *
from tkinter import messagebox

class Tela:
    def __init__(self):
        self.janela = Tk()
        self.botao = Button(self.janela, width = 50,
                            height = 30,
                            text = "Clique aqui",
                            command=self.apertou)
        self.botao.bind("<Enter>", self.passou)
        self.botao.bind("<Leave>", self.saiu)
        self.botao.pack(side = LEFT, padx=20, pady=20)

        mainloop()

    def apertou(self):
        messagebox.showinfo("Mensagem", "Você apertou o botão")

    def passou(self, event):
        event.widget.config(relief = RIDGE)

    def saiu(self, event):
        event.widget.config(relief = RAISED)

minhaTela = Tela()

#RAISED = ACIMA DA INTERFACE (PADRÃO)
#GROOVE = MESMA ALTURA DA INTERFACE
#SUNKEN = ABAIXO DA INTERFACE
#FLAT = SEM CONTORNO
#RIDGE = CONTORNO BRANCO





               
