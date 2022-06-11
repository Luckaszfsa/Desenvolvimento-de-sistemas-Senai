from tkinter import *


class Gerente:
    def __init__(self):
        self.janela = Tk()
        self.janela.title('Menu Gerente')
        self.titleStyles = ('Arial', 14)
        self.textStyles = ('Roboto', 14)
        self.imgStyles = ('Roboto', 15)
        self.janela.state("zoomed")
        
        self.img = PhotoImage(master=self.janela, file="gerente.png")
        self.img1 = self.img.subsample(1, 1)

        self.localIMG = Label(self.janela, image=self.img1)
        self.localIMG.pack(fill='both', anchor='nw')


        self.botaoGerenciar = Button(self.localIMG, command=self.gerenciarFuncionarios,font=self.textStyles,text='Gerenciar\nFuncionários', width=20, height=2)
        self.botaoGerenciar.bind("<Enter>", self.hoverIn)
        self.botaoGerenciar.bind("<Leave>", self.hoverOut)
        self.botaoGerenciar.place(x=810, y=150)

        self.botaoOrdem = Button(self.localIMG, command=self.verOrdem,font=self.textStyles,text='Ordens de Serviços', width=20, height=2)
        self.botaoOrdem.bind("<Enter>", self.hoverIn)
        self.botaoOrdem.bind("<Leave>", self.hoverOut)
        self.botaoOrdem.place(x=810, y=250)

        self.botaoCliente = Button(self.localIMG, command=self.verCliente, font=self.textStyles, text='Cliente',width=20, height=2)
        self.botaoCliente.bind("<Enter>", self.hoverIn)
        self.botaoCliente.bind("<Leave>", self.hoverOut)
        self.botaoCliente.place(x=810, y=350)

        self.botaoSair = Button(self.localIMG, command=self.sair,font=self.textStyles,text='Sair',width=15, height=2)
        self.botaoSair.bind("<Enter>", self.hoverIn2)
        self.botaoSair.bind("<Leave>", self.hoverOut)
        self.botaoSair.place(x=837, y=500)


        mainloop()

    def gerenciarFuncionarios(self):
        from cadastrarFuncionario import ver_cadastrar_func
        ver_cadastrar_func()
        return

    def verOrdem(self):
        return

    def verCliente(self):
        return

    def sair(self):
        return self.janela.destroy()

    def hoverIn(self, event):
        event.widget.config(bg="#1E90FF", fg="white")

    def hoverIn2(self, event):
        event.widget.config(bg="#FF0000", fg="white")

    def hoverOut(self, event):
        event.widget.config(bg="white", fg="black")


minhaTela = Gerente()
