import sqlite3

class Banco():
   def __init__(self):
      self.conexao = sqlite3.connect('banco.db')
      self.criarTabela()

   def criarTabela(self):
      c = self.conexao.cursor()
      c.execute(
            """CREATE TABLE IF NOT EXISTS funcionario(idfunc INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, cpf INTEGER NOT NULL, cargo TEXT NOT NULL, login UNIQUE NOT NULL, senha TEXT NOT NULL)""")
      self.conexao.commit()
      c.close()
