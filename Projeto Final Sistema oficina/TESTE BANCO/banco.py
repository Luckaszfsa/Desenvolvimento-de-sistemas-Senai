import sqlite3

class Banco():
    def __init__(self):

        self.conexao = sqlite3.connect("banco.db")

        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists
        clientes(
        idcliente integer primary key autoincrement,
        nome text NOT NULL,
        cpf integer primary key NOT NULL,
        email text NOT NULL,
        telefone text NOT NULL,
        endereco text NOT NULL,
        carro text NOT NULL,
        placa text NOT NULL)
        """)

        c.execute("""create table if not exists
        usuarios(
        idusuario integer primary key autoincrement,
        nome text NOT NULL,
        cpf integer primary key NOT NULL,
        cargo text NOT NULL,
        senha text NOT NULL)
        """)

        c.execute("""create table if not exists
        orcamentos(
        idorcamento integer primary key autoincrement,
        nome text,
        cpfcliente integer ,
        nomemecanico text,
        carro text,
        placa text,
        servico text,
        valor real)
        """)

        c.execute("""create table if not exists
        orcamentos(
        idorcamento integer primary key autoincrement,
        nomecliente text NOT NULL,
        cpfcliente integer NOT NULL,
        nome_mecanico text NOT NULL,
        carro text NOT NULL,
        placa text NOT NULL,
        servico text NOT NULL,
        valor real NOT NULL)
        """)

        c.execute("""create table if not exists
        ordemservico(
        idordem integer primary key autoincrement,
        nomecliente text NOT NULL,
        nome_mecanico text NOT NULL,
        carro text NOT NULL,
        placa text NOT NULL,
        servico text NOT NULL,
        valor real NOT NULL)
        """

        

        self.conexao.commit()
        c.close()






        
    
