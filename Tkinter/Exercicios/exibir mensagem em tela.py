from tkinter import *
class Interface:
    def __init__(self):
        self.janela = Tk()
        self.frame_cima = Frame(
            master=self.janela)
        self.frame_meio = Frame(
            master=self.janela)
        self.frame_baixo = Frame(
            master=self.janela)

        self.msg = Label(master=self.frame_cima,
                         text="Digite seu nome:")
        self.msg.pack(side="left")
        self.entrada = Entry(
            master=self.frame_cima, width=30)
        self.entrada.pack(side="left")

        self.botao = Button(
            master=self.frame_meio, text="Exibir",
            command=self.exibe)
        self.botao.pack(side="left")
        
        self.resposta = Label(
            master=self.frame_baixo,
            text = "Seu nome é: ")
        self.resposta.pack(side="left")
        self.variavelDinamica = StringVar()
        self.resposta2 = Label(
            master=self.frame_baixo,
            textvariable=self.variavelDinamica)
        self.resposta2.pack(side="left")
                            
        self.frame_cima.pack()
        self.frame_meio.pack()
        self.frame_baixo.pack()
        mainloop()
        
    def exibe(self):
        nome = self.entrada.get()
        self.variavelDinamica.set(nome)

minhaInterface = Interface()

