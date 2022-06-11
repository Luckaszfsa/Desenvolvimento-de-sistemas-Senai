import sqlite3


class Banco():
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.criarTabela()

    def criarTabela(self):
        c = self.conexao.cursor()
        c.execute(
            """CREATE TABLE IF NOT EXISTS clientes(idcliente INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, cpf INTEGER NOT NULL, carro TEXT NOT NULL, telefone TEXT NOT NULL, email TEXT NOT NULL, endereco TEXT NOT NULL)""")
        self.conexao.commit()
        c.close()
