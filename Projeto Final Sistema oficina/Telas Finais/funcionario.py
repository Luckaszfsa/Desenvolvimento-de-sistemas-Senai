from bancoGerente import Banco  # ---- database
from tkinter import messagebox
import tkinter as tk


class TabFunc(object):
    def __init__(self):

        self.info = {}
        self.idfunc = 0
        self.nome = ''
        self.cpf = ''
        self.cargo = ''
        self.login = ''
        self.senha = ''

    def add_func(self):
        b = Banco()
        try:
            c = b.conexao.cursor()
            c.execute("INSERT INTO funcionario(nome, cpf, cargo, login, senha)values('"+self.nome +
                      "', '"+self.cpf+"', '"+self.cargo+"', '"+self.login+"', '"+self.senha+"')")
            b.conexao.commit()
            c.close()
            return messagebox.showinfo('Informativo', 'Funcionário cadastrado com sucesso!')
        except:
            return messagebox.showwarning('Atenção', 'Ocorreu um erro no cadastro')

    def identificar_linha(self, identificador):

        b = Banco()
        c = b.conexao.cursor()
        c.execute("select * from funcionario where idfunc = " +
                  identificador + " ")

        for linha in c:
            self.idfunc = linha[0]
            self.nome = linha[1]
            self.cpf = linha[2]
            self.cargo = linha[3]
            self.login = linha[4]
            self.senha = linha[5]
        c.close()

    def filtrar_func(self, nome):
        b = Banco()
        c = b.conexao.cursor()
        c.execute("SELECT * FROM funcionario WHERE nome LIKE '%"+nome+"%' ")
        linha = c.fetchall()
        c.close()
        return linha

    def populate(self):
        b = Banco()
        c = b.conexao.cursor()
        c.execute('SELECT * FROM funcionario')
        res = c.fetchall()
        c.close()
        return res

    def atualizar_func(self):
        b = Banco()
        try:
            c = b.conexao.cursor()
            c.execute("UPDATE funcionario SET nome = '" +
                      self.nome + "', cpf = '" +
                      self.cpf + "', cargo = '" +
                      self.cargo + "', login = '" +
                      self.login + "', senha = '" +
                      self.senha + "' WHERE idfunc = " +
                      self.idfunc + " ")
            b.conexao.commit()
            c.close()
            return messagebox.showinfo('Informativo', 'Alteração realizada com sucesso!')
        except:
            return messagebox.showwarning('Atenção', 'Ocorreu um erro ao alterar')

    def deletar_func(self):
        b = Banco()
        try:
            c = b.conexao.cursor()
            c.execute("DELETE FROM funcionario WHERE idfunc = " +
                      self.idfunc+" ")
            b.conexao.commit()
            c.close()
            return messagebox.showinfo('Informe', 'funcionário excluído com sucesso!')
        except:
            return messagebox.showwarning('Atenção!', 'Não foi possível excluir funcionário.')
