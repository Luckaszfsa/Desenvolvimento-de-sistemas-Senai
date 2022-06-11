from Tela import *
import Banco as core

app = Tela()

def view_command():
    linhas = core.view()
    app.listClientes.delete(0, END)
    for i in linhas:
        app.listClientes.insert(END, i)

def search_command():
    app.listClientes.delete(0, END)
    linhas = core.search(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    for i in linhas:
        app.listClientes.insert(END, i)

def insert_command():
    core.insert(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    view_command()

def getSelectRow(event):
    global selected
    index = app.listClientes.curselection()[0]
    selected = app.listClientes.get(index)

    app.entNome.delete(0, END)
    app.entSobrenome.delete(0, END)
    app.entEmail.delete(0, END)
    app.entCPF.delete(0, END)

    app.entNome.insert(END, selected[1])
    app.entSobrenome.insert(END, selected[2])
    app.entEmail.insert(END, selected[3])
    app.entCPF.insert(END, selected[4])

def update_command():
    core.update(selected[0], app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    view_command()

def delete_command():
    id = selected[0]
    core.delete(id)
    view_command()

app.verTodos.configure(command = view_command)
app.buscar.configure(command = search_command)
app.inserir.configure(command = insert_command)
app.atualizar.configure(command = update_command)
app.deletar.configure(command = delete_command)
app.fechar.configure(command = app.janela.destroy)
app.listClientes.bind('<<ListboxSelect>>', getSelectRow)
app.executar()