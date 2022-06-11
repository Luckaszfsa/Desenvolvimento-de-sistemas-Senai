from tkinter import *
import datetime

class Tela:
    def __init__(self):
        self.janela = Tk()
        self.relogio = Label(self.janela,
                             font=("Arial", 18),
                                   fg = "blue")
        self.relogio.pack(pady=30, padx=30)
        self.alteraHora()

        mainloop()

    def alteraHora(self):

        agora = datetime.datetime.now()
        self.relogio["text"] = agora.strftime("%H:%M:%S")
        self.janela.after(1000, self.alteraHora)

minhaTela = Tela()







                          

        
