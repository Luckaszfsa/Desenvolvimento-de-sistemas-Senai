from tkinter import *

class Tela:
    def __init__(self):
        self.janela = Tk()

        self.valor = StringVar()

        self.rb1 = Radiobutton(self.janela,
                               text="Python",
                               variable = self.valor,
                               value = "Python",
                               command=self.mostrar)
        self.rb1.pack()
        self.rb1.select()

        self.rb2 = Radiobutton(self.janela,
                               text="Java",
                               variable = self.valor,
                               value = "Java",
                               command=self.mostrar)
        self.rb2.pack()

        self.rb3 = Radiobutton(self.janela,
                               text="C++",
                               variable = self.valor,
                               value = "C++",
                               command=self.mostrar)
        self.rb3.pack()

        self.saida = Label(self.janela)
        self.saida.pack()

        mainloop()

    def mostrar(self):
        escolha = self.valor.get()
        if(escolha == "Python"):
            self.saida["text"] = "print('Hello World')"
        elif(escolha == "Java"):
            self.saida["text"] = "System.out.println('Hello World')"
        else:
            self.saida["text"] = "std::cout << 'Hello World' << std::endl"

minhaTela = Tela()









        
