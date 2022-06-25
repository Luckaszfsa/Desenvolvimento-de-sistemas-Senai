from banco import Banco

class Usuarios(object):

    def __init__(self):

        self.info = {}
        self.idusuario = 0
        self.nome = ""
        self.telefone = ""
        self.email = ""
        self.usuario = ""
        self.senha = ""

    def insertUser(self):
        b = Banco()
        try:
            c = b.conexao.cursor()

            c.execute("insert into usuarios(nome, telefone, email, usuario, senha)values('"+self.nome+
                      "','"+self.telefone+"','"+self.email+"', '"+
                      self.usuario+"', '"+self.senha+"')")

            b.conexao.commit()
            c.close()

            return "Usuario cadastrado com sucesso!"

        except:

            return "Ocorreu um erro no cadastro"

    def updateUser(self):
        
        b = Banco()
        try:
            c = b.conexao.cursor()

            c.execute("update usuarios set nome = '" +
                      self.nome + "', telefone = '" +
                      self.telefone + "', email = '" +
                      self.email + "', usuario = '" +
                      self.usuario + "', senha = '" +
                      self.senha + "' where idusuario = " +
                      self.idusuario+ " ")

            b.conexao.commit()
            c.close()

            return "Usuario atualizado com sucesso!"

        except:

            return "Ocorreu um erro na alteração"

    def deleteUser(self):

        b = Banco()
        try:
            c = b.conexao.cursor()

            c.execute("delete from usuarios where idusuario = " + self.idusuario +" ")

            b.conexao.commit()
            c.close()

            return "Usuário excluido com sucesso"

        except:

            return "Ocorreu um erro na exclusão"

    def selectUser(self, idusuario):
        
        b = Banco()
        try:
            c = b.conexao.cursor()

            c.execute("select * from usuarios where idusuario = "+
                      idusuario+ " ")

            for linha in c:
                self.idusuario = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.usuario = linha[4]
                self.senha = linha[5]

            c.close()

            return "Busca feita com sucesso"

        except:

            return "Ocorreu um erro na busca"
                









            

        
