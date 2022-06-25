<<<<<<< HEAD
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from turtle import bgcolor, heading
from bd import Database

db = Database("funcionarios.db")
janela = Tk()
janela.title("Sistema de gerenciamento de funcionários")
janela.geometry("1920x1080")
janela.config(bg = "#2c3e50")
janela.state("zoomed")

nome = StringVar()
idade = IntVar()
idade.set("")
dataN = StringVar()
genero = StringVar()
email = StringVar()
telefone =StringVar()

frame1 = Frame(janela, bg = "#535c68")
frame1.pack(fill=X)
titulo = Label(frame1, text = "Sistema de Gerenciamento de funcionários", font=("Calibri", 18, "bold"), bg=
 "#535c68",fg="white")
titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")

labelNome = Label(frame1, text="Nome", bg="#535c68", font=("Calibri", 16), fg="white")
labelNome.grid(row=1, column=0, padx=10, pady=10, sticky="w")
txtNome = Entry(frame1, textvariable=nome, font=("Calibri", 16), width=30)
txtNome.grid(row=1, column=1, padx=10, pady=10, sticky="w")

labelIdade = Label(frame1, text="Idade", bg="#535c68", font=("Calibri", 16), fg="white")
labelIdade.grid(row=1, column=2, padx=10, pady=10, sticky="w")
txtIdade = Entry(frame1, textvariable=idade, font=("Calibri", 16), width=30)
txtIdade.grid(row=1, column=3, padx=10, pady=10, sticky="w")

labelDataN = Label(frame1, text="Data de Nascimento", bg="#535c68", font=("Calibri", 16), fg="white")
labelDataN.grid(row=2, column=0, padx=10, pady=10, sticky="w")
txtDataN = Entry(frame1, textvariable=dataN, font=("Calibri", 16), width=30)
txtDataN.grid(row=2, column=1, padx=10, pady=10, sticky="w")

labelEmail = Label(frame1, text="Email", bg="#535c68", font=("Calibri", 16), fg="white")
labelEmail.grid(row=2, column=2, padx=10, pady=10, sticky="w")
txtEmail = Entry(frame1, textvariable=email, font=("Calibri", 16), width=30)
txtEmail.grid(row=2, column=3, padx=10, pady=10, sticky="w")

labelGenero = Label(frame1, text="Gênero", bg="#535c68", font=("Calibri", 16), fg="white")
labelGenero.grid(row=3, column=0, padx=10, pady=10, sticky="w")
comboGenero = ttk.Combobox(frame1, textvariable=genero, font=("Calibri", 16), width=28, state="readonly")
comboGenero["values"] = ("Masculino", "Feminino")
comboGenero.grid(row=3, column=1, padx=10, sticky="w")

labelTelefone = Label(frame1, text="Telefone", bg="#535c68", font=("Calibri", 16), fg="white")
labelTelefone.grid(row=3, column=2, padx=10, pady=10, sticky="w")
txtTelefone = Entry(frame1, textvariable=telefone, font=("Calibri", 16), width=30)
txtTelefone.grid(row=3, column=3, padx=10, pady=10, sticky="w")

labelEndereco = Label(frame1, text="Endereco", bg="#535c68", font=("Calibri", 16), fg="white")
labelEndereco.grid(row=4, column=0, padx=10, pady=10, sticky="w")
txtEndereco = Text(frame1, font=("Calibri", 16), width=90, height=5)
txtEndereco.grid(row=5, column=0, padx=10, sticky="w", columnspan=4)

def getData(event):
    #pega a linha da tabela onde o ponteiro do mouse está quando o evento disparado
    selected_row = tv.focus()
    #pega o item(funcionário) que está nessa linha da tabela
    data = tv.item(selected_row)
    global row
    row = data["values"]
    nome.set(row[1])
    idade.set(row[2])
    dataN.set(row[3])
    email.set(row[4])
    genero.set(row[5])
    telefone.set(row[6])
    txtEndereco.delete(1.0, END)
    txtEndereco.insert(END, row[7])

def displayAll():
    tv.delete(*tv.get_children())
    for i in db.fetch():
        tv.insert("", END, values=i)

def add_funcionario():
    if(txtNome.get() == "" or txtIdade.get() == "" or txtDataN.get() == "" or txtEmail.get() == "" or comboGenero.get() == "" or txtTelefone.get() == "" or txtEndereco.get(1.0, END) == ""):
        messagebox.showerror("Erro na entrada", "Por favor, preencha todos os campos")
    else:
        db.insert(txtNome.get(), txtIdade.get(), txtDataN.get(), txtEmail.get(), comboGenero.get(), txtTelefone.get(), txtEndereco.get(1.0, END))
        messagebox.showinfo("Sucesso", "Funcionário cadastrado")
        clearAll()
        displayAll()

def edit_funcionario():
    if(txtNome.get() == "" or txtIdade.get() == "" or txtDataN.get() == "" or txtEmail.get() == "" or comboGenero.get() == "" or txtTelefone.get() == "" or txtEndereco.get(1.0, END) == ""):
        messagebox.showerror("Erro na entrada", "Por favor, preencha todos os campos")
    else:
        db.update(row[0], txtNome.get(), txtIdade.get(), txtDataN.get(), txtEmail.get(), comboGenero.get(), txtTelefone.get(), txtEndereco.get(1.0, END))
        messagebox.showinfo("Sucesso", "Funcionário atualizado")
        clearAll()
        displayAll()

def del_funcionario():
    db.remove(row[0])
    clearAll()
    displayAll()

def clearAll():
    nome.set("")
    idade.set("")
    dataN.set("")
    genero.set("")
    email.set("")
    telefone.set("")
    txtEndereco.delete(1.0, END)

frame2 = Frame(frame1, bg="#535c68")
frame2.grid(row = 6, column=0, columnspan=4, padx=10,pady=10, sticky="w")

add = Button(frame2, command=add_funcionario, text="Adicionar", width=15, font=("Calibri", 16, "bold"), fg="white", bg="#16a085")
add.grid(row=0, column=0, padx=10)

edit = Button(frame2, command=edit_funcionario, text="Editar", width=15, font=("Calibri", 16, "bold"), fg="white", bg="#2980b9")
edit.grid(row=0, column=1, padx=10)

delete = Button(frame2, command=del_funcionario, text="Deletar", width=15, font=("Calibri", 16, "bold"), fg="white", bg="#c0392b")
delete.grid(row=0, column=2, padx=10)

clear = Button(frame2, command=clearAll, text="Limpar Campos", width=15, font=("Calibri", 16, "bold"), fg="white", bg="#f39c12")
clear.grid(row=0, column=3, padx=10)

frame3 = Frame(janela, bg="#ecf0f1")
frame3.place(x=0, y=480, width=1980, height=520)

#Criando e configurando o estilo de tabela que será criada
style = ttk.Style()
style.configure("mystyle.Treeview", font=("Calibri", 14), rowheight=50)
style.configure("mystyle.Treeview.Heading", font=("Calibri", 14))
#Criando a tabela de fato
tv = ttk.Treeview(frame3, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=4, stretch=NO)
tv.heading("2", text="Nome")
tv.column("2", width=300, stretch=NO)
tv.heading("3", text="Idade")
tv.column("3", width=60, stretch=NO)
tv.heading("4", text="Data de Nascimento")
tv.column("4", width=165, stretch=NO)
tv.heading("5", text="Email")
tv.column("5", width=200, stretch=NO)
tv.heading("6", text="Gênero")
tv.column("6", width=150, stretch=NO)
tv.heading("7", text="Telefone")
tv.column("7", width=150, stretch=NO)
tv.heading("8", text="Endereço")
tv.column("8", width=300, stretch=NO)
tv["show"] = "headings"
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

displayAll()

janela.mainloop()

=======
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from turtle import bgcolor, heading
from bd import Database

db = Database("funcionarios.db")
janela = Tk()
janela.title("Sistema de gerenciamento de funcionários")
janela.geometry("1920x1080")
janela.config(bg = "#2c3e50")
janela.state("zoomed")

nome = StringVar()
idade = IntVar()
idade.set("")
dataN = StringVar()
genero = StringVar()
email = StringVar()
telefone =StringVar()

frame1 = Frame(janela, bg = "#535c68")
frame1.pack(fill=X)
titulo = Label(frame1, text = "Sistema de Gerenciamento de funcionários", font=("Calibri", 18, "bold"), bg=
 "#535c68",fg="white")
titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")

labelNome = Label(frame1, text="Nome", bg="#535c68", font=("Calibri", 16), fg="white")
labelNome.grid(row=1, column=0, padx=10, pady=10, sticky="w")
txtNome = Entry(frame1, textvariable=nome, font=("Calibri", 16), width=30)
txtNome.grid(row=1, column=1, padx=10, pady=10, sticky="w")

labelIdade = Label(frame1, text="Idade", bg="#535c68", font=("Calibri", 16), fg="white")
labelIdade.grid(row=1, column=2, padx=10, pady=10, sticky="w")
txtIdade = Entry(frame1, textvariable=idade, font=("Calibri", 16), width=30)
txtIdade.grid(row=1, column=3, padx=10, pady=10, sticky="w")

labelDataN = Label(frame1, text="Data de Nascimento", bg="#535c68", font=("Calibri", 16), fg="white")
labelDataN.grid(row=2, column=0, padx=10, pady=10, sticky="w")
txtDataN = Entry(frame1, textvariable=dataN, font=("Calibri", 16), width=30)
txtDataN.grid(row=2, column=1, padx=10, pady=10, sticky="w")

labelEmail = Label(frame1, text="Email", bg="#535c68", font=("Calibri", 16), fg="white")
labelEmail.grid(row=2, column=2, padx=10, pady=10, sticky="w")
txtEmail = Entry(frame1, textvariable=email, font=("Calibri", 16), width=30)
txtEmail.grid(row=2, column=3, padx=10, pady=10, sticky="w")

labelGenero = Label(frame1, text="Gênero", bg="#535c68", font=("Calibri", 16), fg="white")
labelGenero.grid(row=3, column=0, padx=10, pady=10, sticky="w")
comboGenero = ttk.Combobox(frame1, textvariable=genero, font=("Calibri", 16), width=28, state="readonly")
comboGenero["values"] = ("Masculino", "Feminino")
comboGenero.grid(row=3, column=1, padx=10, sticky="w")

labelTelefone = Label(frame1, text="Telefone", bg="#535c68", font=("Calibri", 16), fg="white")
labelTelefone.grid(row=3, column=2, padx=10, pady=10, sticky="w")
txtTelefone = Entry(frame1, textvariable=telefone, font=("Calibri", 16), width=30)
txtTelefone.grid(row=3, column=3, padx=10, pady=10, sticky="w")

labelEndereco = Label(frame1, text="Endereco", bg="#535c68", font=("Calibri", 16), fg="white")
labelEndereco.grid(row=4, column=0, padx=10, pady=10, sticky="w")
txtEndereco = Text(frame1, font=("Calibri", 16), width=90, height=5)
txtEndereco.grid(row=5, column=0, padx=10, sticky="w", columnspan=4)

def getData(event):
    #pega a linha da tabela onde o ponteiro do mouse está quando o evento disparado
    selected_row = tv.focus()
    #pega o item(funcionário) que está nessa linha da tabela
    data = tv.item(selected_row)
    global row
    row = data["values"]
    nome.set(row[1])
    idade.set(row[2])
    dataN.set(row[3])
    email.set(row[4])
    genero.set(row[5])
    telefone.set(row[6])
    txtEndereco.delete(1.0, END)
    txtEndereco.insert(END, row[7])

def displayAll():
    tv.delete(*tv.get_children())
    for i in db.fetch():
        tv.insert("", END, values=i)

def add_funcionario():
    if(txtNome.get() == "" or txtIdade.get() == "" or txtDataN.get() == "" or txtEmail.get() == "" or comboGenero.get() == "" or txtTelefone.get() == "" or txtEndereco.get(1.0, END) == ""):
        messagebox.showerror("Erro na entrada", "Por favor, preencha todos os campos")
    else:
        db.insert(txtNome.get(), txtIdade.get(), txtDataN.get(), txtEmail.get(), comboGenero.get(), txtTelefone.get(), txtEndereco.get(1.0, END))
        messagebox.showinfo("Sucesso", "Funcionário cadastrado")
        clearAll()
        displayAll()

def edit_funcionario():
    if(txtNome.get() == "" or txtIdade.get() == "" or txtDataN.get() == "" or txtEmail.get() == "" or comboGenero.get() == "" or txtTelefone.get() == "" or txtEndereco.get(1.0, END) == ""):
        messagebox.showerror("Erro na entrada", "Por favor, preencha todos os campos")
    else:
        db.update(row[0], txtNome.get(), txtIdade.get(), txtDataN.get(), txtEmail.get(), comboGenero.get(), txtTelefone.get(), txtEndereco.get(1.0, END))
        messagebox.showinfo("Sucesso", "Funcionário atualizado")
        clearAll()
        displayAll()

def del_funcionario():
    db.remove(row[0])
    clearAll()
    displayAll()

def clearAll():
    nome.set("")
    idade.set("")
    dataN.set("")
    genero.set("")
    email.set("")
    telefone.set("")
    txtEndereco.delete(1.0, END)

frame2 = Frame(frame1, bg="#535c68")
frame2.grid(row = 6, column=0, columnspan=4, padx=10,pady=10, sticky="w")

add = Button(frame2, command=add_funcionario, text="Adicionar", width=15, font=("Calibri", 16, "bold"), fg="white", bg="#16a085")
add.grid(row=0, column=0, padx=10)

edit = Button(frame2, command=edit_funcionario, text="Editar", width=15, font=("Calibri", 16, "bold"), fg="white", bg="#2980b9")
edit.grid(row=0, column=1, padx=10)

delete = Button(frame2, command=del_funcionario, text="Deletar", width=15, font=("Calibri", 16, "bold"), fg="white", bg="#c0392b")
delete.grid(row=0, column=2, padx=10)

clear = Button(frame2, command=clearAll, text="Limpar Campos", width=15, font=("Calibri", 16, "bold"), fg="white", bg="#f39c12")
clear.grid(row=0, column=3, padx=10)

frame3 = Frame(janela, bg="#ecf0f1")
frame3.place(x=0, y=480, width=1980, height=520)

#Criando e configurando o estilo de tabela que será criada
style = ttk.Style()
style.configure("mystyle.Treeview", font=("Calibri", 14), rowheight=50)
style.configure("mystyle.Treeview.Heading", font=("Calibri", 14))
#Criando a tabela de fato
tv = ttk.Treeview(frame3, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=4, stretch=NO)
tv.heading("2", text="Nome")
tv.column("2", width=300, stretch=NO)
tv.heading("3", text="Idade")
tv.column("3", width=60, stretch=NO)
tv.heading("4", text="Data de Nascimento")
tv.column("4", width=165, stretch=NO)
tv.heading("5", text="Email")
tv.column("5", width=200, stretch=NO)
tv.heading("6", text="Gênero")
tv.column("6", width=150, stretch=NO)
tv.heading("7", text="Telefone")
tv.column("7", width=150, stretch=NO)
tv.heading("8", text="Endereço")
tv.column("8", width=300, stretch=NO)
tv["show"] = "headings"
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

displayAll()

janela.mainloop()

>>>>>>> a61989a68e483bf4048d714092312fcfae0a4022
