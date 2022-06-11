import sqlite3 as sql

#Classe que gera o bjeto que contém os parametros do
#banco

class Banco():
    database = "clientes.db"
    conn = None
    cursor = None
    connected = False

    #função para criar a conexão com o banco
    def connect(self):
        #criando a conexão entre o sqlite e o nosso
        #arquivo de banco de dados
        Banco.conn = sql.connect(Banco.database)
        #Criando o cursor para alterar o banco
        Banco.cursor = Banco.conn.cursor()
        #Marcação para saber se a conexão foi feita
        Banco.connected = True

    #função para fechar a conexão com o banco
    def disconnect(self):
        #Fechando a conexão entre o sqlite e o nosso
        #arquivo de banco de dados
        Banco.conn.close()
        #Marcação para saber se a conexão foi feita
        Banco.connected =  False

    #função que executa um comando no banco de dados
    #Recebe 3 parametros
    #self
    #sql = comando escrito na linguagem sql a ser feito
    #parms = lista com os parametros do comando
    def execute(self, sql, parms = None):
        #Verificando se a conexão está ativa
        if Banco.connected:
            #Verifica se não há lista de parametros
            if parms == None:
                Banco.cursor.execute(sql)
            else:
                Banco.cursor.execute(sql, parms)
            return True
        else:
            return False

    #Função que recupera os valores recebidos de um select
    def fetchall(self):
        return Banco.cursor.fetchall()

    #Função que realiza o commit das operações executadas
    def persist(self):
        #Verificando se a conexão está ativa
        if Banco.connected:
            Banco.conn.commit()
            return True
        else:
            return False

#Função para iniciar o banco de dados
def initDB():
    #Criando um objeto para usar as funções acima
    banco = Banco()
    #Conectar ao banco
    banco.connect()
    #Executar o comando de criar a tabela
    banco.execute("CREATE TABLE IF NOT EXISTS clientes(id INTEGER PRIMARY KEY, nome TEXT, sobrenome TEXT, email TEXT, cpf TEXT)")
    #Persistir a criação da tabela
    banco.persist()
    #Fechar a conexão
    banco.disconnect()

initDB()

def view():
    #Criando um objeto para usar as funções acima
    banco = Banco()
    #Conectar ao banco
    banco.connect()
    #Executar o comando de selecionar todos os clientes da tabela
    banco.execute("SELECT * FROM clientes")
    #Recuperando os valores
    linhas = banco.fetchall()
    #Fechar a conexão
    banco.disconnect()
    #Retornando os valores
    return linhas

def insert(nome, sobrenome, email, cpf):
    #Criando um objeto para usar as funções acima
    banco = Banco()
    #Conectar ao banco
    banco.connect()
    #Executar o comando para inserir um cliente
    banco.execute("INSERT INTO clientes VALUES(NULL, ?, ?, ?, ?)",(nome, sobrenome, email, cpf))
    #Persistir a inserção do cliente
    banco.persist()
    #Fechar a conexão
    banco.disconnect()

def search(nome = "", sobrenome = "", email = "", cpf = ""):
    #Criando um objeto para usar as funções acima
    banco = Banco()
    #Conectar ao banco
    banco.connect()
    #Executar o comando de buscar clientes
    banco.execute("SELECT * FROM clientes WHERE nome=? OR sobrenome=? OR email=? OR cpf=?", (nome, sobrenome, email, cpf))
    #Recuperando os valores
    linhas = banco.fetchall()
    #Fechar a conexão
    banco.disconnect()
    #Retornando os valores
    return linhas

def update(id, nome, sobrenome, email, cpf):
    #Criando um objeto para usar as funções acima
    banco = Banco()
    #Conectar ao banco
    banco.connect()
    #Executar o comando para atualizar um cliente
    banco.execute("UPDATE clientes SET nome=?, sobrenome=?, email=?, cpf=?WHERE id=?",(nome, sobrenome, email, cpf, id))
    #Persistir a atualização do cliente
    banco.persist()
    #Fechar a conexão
    banco.disconnect()

def delete(id):
    #Criando um objeto para usar as funções acima
    banco = Banco()
    #Conectar ao banco
    banco.connect()
    #Executar o comando para deletar um cliente
    banco.execute("DELETE FROM clientes WHERE id=?",(id, ))
    #Persistir a exclusão do cliente
    banco.persist()
    #Fechar a conexão
    banco.disconnect()