# importações
from pony.orm import *
import os # comandos do sistema operacional

# criando variável de acesso ao pony
db = Database()

# definição da classe: 
# é preciso herdar da classe Entity
class Pessoa(db.Entity):
    nome = Required(str)   # atributo string obrigatório
    email = Required(str, 100)  # atributo string obrigatório com máximo de 100 caracteres
    telefone = Optional(str, nullable=True) # atributo opcional 

# obtendo dados de conexão com o banco, 
# a partir de variáveis de ambiente
dname    = os.getenv("DATABASE_NAME")
host     = os.getenv("DATABASE_HOST")
user     = os.getenv("DATABASE_USER")
password = os.getenv("DATABASE_PASSWORD")
port     = os.getenv("DATABASE_PORT")

db.bind(provider='mysql', host=host, 
        user=user, password=password, database=dname)

# innformando que deve criar as tabelas, caso não existam
db.generate_mapping(create_tables=True)

# solicitando para mostrar os comandos SQL que vão sendo executados
#set_sql_debug(True)

# iniciando uma sessão
with db_session:

    # criando uma pessoa
    jo = Pessoa(nome='João da Silva', email='josilva@gmail.com')

    # salvando
    commit()

    # exibindo os dados
    print(jo.nome, jo.email)
    
    # existe um ID?
    print(jo.id)

'''
Exercícios:

1) Conecte-se a um banco de dados MySql com o DBeaver para ver se
a tabela foi criada e os dados estão lá

2) Descomente a linha 30 e execute novamente o programa, para ver
os códigos SQL que estão sendo executados

'''