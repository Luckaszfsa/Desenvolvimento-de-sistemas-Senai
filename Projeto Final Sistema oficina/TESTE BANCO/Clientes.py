from banco import Banco

class Clientes(object):

    def __init__(self):

        self.info = {}
        self.idcliente = 0
        self.nome = ""
        self.cpf = 0
        self.email = ""
        self.telefone = ""
        self.endereco = ""
        self.carro = ""
        self.placa = ""

    def insertUser(self):
        b = Banco()
        try:
            c = b.conexao.cursor()

            c.execute("insert into clientes(nome, cpf, email, telefone, endereco, carro, placa)values('"+self.nome+
                      "','"+self.cpf+"','"+self.email+"','"+self.telefone+'", '"+
                      self.endereco+"', '"+self.carro+"', '"+self.placa+"')")

            b.conexao.commit()
            c.close()

            return "Cliente cadastrado com sucesso!"

        except:

            return "Ocorreu um erro no cadastro"

    def updateUser(self):
        
        b = Banco()
        try:
            c = b.conexao.cursor()

            c.execute("update clientes set nome = '" +
                      self.nome + "',cpf = '" +
                      self.cpf + "', email = '" +
                      self.email + "',telefone = '" +
                      self.telefone + "', endereco = '" +
                      self.endereco + "', carro = '" +
                      self.carro + "', placa = '" +
                      self.placa + "' where idcliente = " +
                      self.idcliente+ " ")

            b.conexao.commit()
            c.close()

            return "Cliente atualizado com sucesso!"

        except:

            return "Ocorreu um erro na alteração"

    def deleteUser(self):

        b = Banco()
        try:
            c = b.conexao.cursor()

            c.execute("delete from clientes where idcliente = " + self.idcliente +" ")

            b.conexao.commit()
            c.close()

            return "Cliente excluido com sucesso"

        except:

            return "Ocorreu um erro na exclusão"

    def selectUser(self, idcliente):
        
        b = Banco()
        try:
            c = b.conexao.cursor()

            c.execute("select * from clientes where idcliente = "+
                      idcliente+ " ")

            for linha in c:
                self.idcliente = linha[0]
                self.nome = linha[1]
                self.cpf = linha[2]
                self.email = linha[3]
                self.telefone = linha[4]
                self.endereco = linha[5]
                self.carro = linha[6]
                self.placa = linha[7]

            c.close()

            return "Busca feita com sucesso"

        except:

            return "Ocorreu um erro na busca"
                









            

        
