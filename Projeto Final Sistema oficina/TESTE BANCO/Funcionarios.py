from banco import Banco

class Funcionarios(object):

    def __init__(self):

        self.info = {}
        self.idfuncionario = 0
        self.nome = ""
        self.cpf = 0
        self.cargo = ""
        self.senha = ""
        

    def insertUser(self):
        b = Banco()
        try:
            c = b.conexao.cursor()

            c.execute("insert into clientes(nome, cpf, cargo, senha)values('"+self.nome+
                      "','"+self.cpf+"','"+self.cargo+"','"+self.senha+'")")

            b.conexao.commit()
            c.close()

            return "Funcionário cadastrado com sucesso!"

        except:

            return "Ocorreu um erro no cadastro"

    def updateUser(self):
        
        b = Banco()
        try:
            c = b.conexao.cursor()

            c.execute("update funcionarios set nome = '" +
                      self.nome + "',cpf = '" +
                      self.cpf + "', cargo = '" +
                      self.cargo + "',senha = '" +
                      self.senha + "' where idfuncionario = " +
                      self.idfuncionario+ " ")

            b.conexao.commit()
            c.close()

            return "Funcionário atualizado com sucesso!"

        except:

            return "Ocorreu um erro na alteração"

    def deleteUser(self):

        b = Banco()
        try:
            c = b.conexao.cursor()

            c.execute("delete from funcionarios where idfuncionario = " + self.idfuncionario +" ")

            b.conexao.commit()
            c.close()

            return "Funcionário excluido com sucesso"

        except:

            return "Ocorreu um erro na exclusão"

    def selectUser(self, idfuncionario):
        
        b = Banco()
        try:
            c = b.conexao.cursor()

            c.execute("select * from funcionarios where idfuncionario = "+
                      idfuncionario+ " ")

            for linha in c:
                self.idfuncionario = linha[0]
                self.nome = linha[1]
                self.cpf = linha[2]
                self.cargo = linha[3]
                self.senha = linha[4]
                

            c.close()

            return "Busca feita com sucesso"

        except:

            return "Ocorreu um erro na busca"
                









            

        
