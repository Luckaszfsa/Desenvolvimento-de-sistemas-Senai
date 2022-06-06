from meubanco import Banco  # ---- database
from tkinter import messagebox
import tkinter as tk


class Clientes(object):
    def __init__(self):

        self.info = {}
        self.idcliente = 0
        self.nome = ''
        self.cpf = ''
        self.carro = ''
        self.telefone = ''
        self.email = ''
        self.endereco = ''

    def add_cliente(self):
        b = Banco()
        try:
            c = b.conexao.cursor()
            c.execute("INSERT INTO clientes(nome, cpf, carro, telefone, email, endereco)values('"+self.nome +
                      "', '"+self.cpf+"', '"+self.carro+"', '"+self.telefone+"', '"+self.email+"', '"+self.endereco+"')")
            b.conexao.commit()
            c.close()
            return messagebox.showinfo('Informativo', 'Cliente cadastrado com sucesso!')
        except:
            return messagebox.showwarning('Atenção', 'Ocorreu um erro no cadastro')

    def identificar_linha(self, identificador):

        b = Banco()
        c = b.conexao.cursor()
        c.execute("select * from clientes where idcliente = "+ identificador + " ")
        
        for linha in c:
            self.idcliente = linha[0]
            self.nome = linha[1]
            self.cpf = linha[2]
            self.carro = linha[3]
            self.telefone = linha[4]
            self.email = linha[5]
            self.endereco = linha[6]
        c.close()

    def buscar_cliente(self, nome):
        b = Banco()
        try:
            c = b.conexao.cursor()
            c.execute("SELECT * FROM clientes WHERE nome LIKE '%"
                      + nome+"%' ")
            for linha in c:
                self.idcliente = linha[0]
                self.nome = linha[1]
                self.cpf = linha[2]
                self.carro = linha[3]
                self.telefone = linha[4]
                self.email = linha[5]
                self.endereco = linha[6]

            c.close()
            return messagebox.showinfo('INFORMATIVO', 'Cliente Encontrado!')

        except:
            return messagebox.showwarning('ATENÇÃO', 'Cliente Não Encontrado')

    def populate(self):
        b = Banco()
        c = b.conexao.cursor()
        c.execute('SELECT * FROM clientes')
        res = c.fetchall()
        c.close()
        return res

    # def filtrar(nome):
    #     b = Banco()
    #     c = b.conexao.cursor()
    #     c.execute("SELECT * FROM clientes WHERE nome LIKE '%"
    #                   + nome+"%' ")
    #     res = c.fetchall()
    #     c.close()
    #     return res

    def atualizar_cliente(self):
        b = Banco()
        try:
            c = b.conexao.cursor()
            c.execute("UPDATE clientes SET nome = '" +
                      self.nome + "', cpf = '" +
                      self.cpf + "', carro = '" +
                      self.carro + "', telefone = '" +
                      self.telefone + "', email = '" +
                      self.email + "', endereco = '" +
                      self.endereco + "' WHERE idcliente = " +
                      self.idcliente + " ")
            b.conexao.commit()
            c.close()
            return messagebox.showinfo('Informativo', 'Alteração realizada com sucesso!')
        except:
            return messagebox.showwarning('Atenção', 'Ocorreu um erro ao alterar')

    def deletar_cliente(self):
        b = Banco()
        try:
            c = b.conexao.cursor()
            c.execute("DELETE FROM clientes WHERE idcliente = " +
                      self.idcliente+" ")
            b.conexao.commit()
            c.close()
            return messagebox.showinfo('Informe', 'Cliente excluído com sucesso!')
        except:
            return messagebox.showwarning('Atenção!', 'Não foi possível excluir cliente.')
