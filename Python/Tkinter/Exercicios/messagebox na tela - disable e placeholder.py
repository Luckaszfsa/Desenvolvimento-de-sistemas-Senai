from tkinter import *
from tkinter import messagebox

class Tela:
    def __init__(self):
        self.janela = Tk()
        self.caixa1 = Entry(self.janela, name = "caixa1")
        self.caixa1.bind("<Return>", self.exibe)
        self.caixa1.pack(side = LEFT, padx=5)

        self.caixa2 = Entry(self.janela, name = "caixa2")
        self.caixa2.insert(INSERT, "Digite um texto aqui")
        self.caixa2.bind("<Return>", self.exibe)
        self.caixa2.pack(side = LEFT, padx=5)

        self.frame = Frame(self.janela)
        self.frame.pack(side = BOTTOM, pady=5)

        self.caixa3 = Entry(self.frame, name = "caixa3")
        self.caixa3.insert(INSERT, "Texto não editavel")
        self.caixa3.config(state = DISABLED)
        self.caixa3.bind("<Return>", self.exibe)
        self.caixa3.pack()

        mainloop()

    def exibe(self, event):
        nomeCaixa = event.widget.winfo_name()
        conteudoCaixa = event.widget.get()
        messagebox.showinfo("Texto na caixa",
                            "Nome do componente: "
                            +nomeCaixa + "\nContéudo: "
                            + conteudoCaixa)
        
minhaTela = Tela()












        
        
