from tkinter import *

class Tela:

    janela = Tk()

    janela.wm_title("Cadastro de Clientes")

    txtNome = StringVar()
    txtSobrenome = StringVar()
    txtEmail = StringVar()
    txtCPF = StringVar()

    labelNome = Label(janela, text="Nome")
    labelSobrenome = Label(janela, text="Sobrenome")
    labelEmail = Label(janela, text="Email")
    labelCPF = Label(janela, text="CPF")

    entNome = Entry(janela, textvariable=txtNome)
    entSobrenome = Entry(janela, textvariable=txtSobrenome)
    entEmail = Entry(janela, textvariable=txtEmail)
    entCPF = Entry(janela, textvariable=txtCPF)

    listClientes = Listbox(janela, width=100)

    scrollClientes = Scrollbar(janela)

    verTodos = Button(janela, text="Ver Todos")
    buscar = Button(janela, text="Buscar")
    inserir = Button(janela, text="Inserir")
    atualizar = Button(janela, text="Atualizar Selecionado")
    deletar = Button(janela, text="Deletar Selecionado")
    fechar = Button(janela, text="Fechar")

    labelNome.grid(row=0, column=0)
    labelSobrenome.grid(row=1, column=0)
    labelEmail.grid(row=2, column=0)
    labelCPF.grid(row=3, column=0)

    entNome.grid(row=0, column=1)
    entSobrenome.grid(row=1, column=1)
    entEmail.grid(row=2, column=1)
    entCPF.grid(row=3, column=1)

    listClientes.grid(row=0, column=2, rowspan=10)

    scrollClientes.grid(row=0, column=6, rowspan=10)

    verTodos.grid(row=4, column=0, columnspan=2)
    buscar.grid(row=5, column=0,columnspan=2)
    inserir.grid(row=6, column=0,columnspan=2)
    atualizar.grid(row=7, column=0,columnspan=2)
    deletar.grid(row=8, column=0,columnspan=2)
    fechar.grid(row=9, column=0,columnspan=2)

    listClientes.configure(yscrollcommand = scrollClientes.set)

    scrollClientes.configure(command = listClientes.yview)

    xPad = 5
    yPad = 3

    #Adicionando um pouco de beleza a interface
    for i in janela.winfo_children():
        widget_class = i.__class__.__name__
        if widget_class == "Button":
            i.grid_configure(sticky = "ew", padx = xPad, pady = yPad)
        elif widget_class == "Listbox":
            i.grid_configure(padx = 0, pady=0, sticky="ns")
        elif widget_class == "Scrollbar":
            i.grid_configure(padx=0, pady=0, sticky="ns")
        else:
            i.grid_configure(padx = xPad, pady = yPad, sticky="n")

    def executar(self):
        Tela.janela.mainloop()
