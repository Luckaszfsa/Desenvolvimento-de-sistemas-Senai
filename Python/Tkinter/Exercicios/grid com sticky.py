from tkinter import *
janela = Tk()
janela.columnconfigure(0, minsize=250)
janela.rowconfigure([0, 1], minsize=100)

label1 = Label(text="A")
label1.grid(row=0, column=0, sticky="NE")

label2 = Label(text="B")
label2.grid(row=1, column=0, sticky="SW")

mainloop()

#"N" ou "n" = Norte
#"S" ou "s" = Sul
#"E" ou "e" = Leste
#"W" ou "w" = Oeste
#"NE" ou "ne" = Nordeste
#"SE" ou "se" = Sudeste
#"NW" ou "nw" = Noroeste
#"SW" ou "sw" = Sudoeste
