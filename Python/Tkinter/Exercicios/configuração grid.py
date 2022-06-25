from tkinter import *
janela = Tk()
janela.rowconfigure(0, minsize=50)
janela.columnconfigure([0, 1, 2, 3], minsize=50)
label1 = Label(text="1", bg="black",
               fg="white")
label1.grid(row=0, column=0)

label2 = Label(text="2", bg="black",
               fg="white")
label2.grid(row=0, column=1, sticky="ns")

label3 = Label(text="3", bg="black",
               fg="white")
label3.grid(row=0, column=2, sticky="ew")

label4 = Label(text="4", bg="black",
               fg="white")
label4.grid(row=0, column=3, sticky="nsew")
mainloop()
