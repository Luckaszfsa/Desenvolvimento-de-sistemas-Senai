from tkinter import *
janela = Tk()
for i in range(3):
    janela.columnconfigure(i, weight=1,
                           minsize=75)
    janela.rowconfigure(i, weight=1,
                        minsize=50)
    for j in range(3):
        frame = Frame(master=janela,
                      relief=RAISED,
                      borderwidth=1)
        frame.grid(row=i, column=j, padx=5,
                   pady=5)
        label = Label(master=frame,
                text=f"Row{i}\nColumn{j}",
                      width = 60, height = 25)
        label.pack(padx=5, pady=5)
mainloop()
