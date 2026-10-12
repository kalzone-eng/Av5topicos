from config import *
from models.pessoa import Pessoa
from routes.pessoa import *
from routes.utils import *
from routes.login import *
from models.aviao import Aviao
from routes.avioes import *

# cria o banco, caso não exista :-/
auxiliar_criar_bd()

if __name__ == '__main__':
    app.run(debug=True)