from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String

# Definindo a classe base para os modelos (padrão SQLAlchemy 2.0)
class Base(DeclarativeBase):
    pass

app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializando SQLAlchemy passando a classe model_class
db = SQLAlchemy(app, model_class=Base)

# Modelo da classe Pessoa estilo 2.0
class Pessoa(db.Model):
    __tablename__ = 'pessoas'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    telefone: Mapped[str] = mapped_column(String(20), nullable=False)

# Cria as tabelas no banco de dados
with app.app_context():
    db.create_all()

# Rota principal: exibe o formulário e a lista de pessoas
@app.route('/')
def index():
    # Consulta no estilo SQLAlchemy 2.0 (db.select)
    query = db.select(Pessoa)
    pessoas = db.session.scalars(query).all()
    return render_template('index.html', pessoas=pessoas)

# Rota para cadastrar uma nova pessoa
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    # pega os dados do formulário
    nome = request.form.get('nome')
    email = request.form.get('email')
    telefone = request.form.get('telefone')

    if nome and email and telefone:
        # cria uma pessoa
        nova_pessoa = Pessoa(nome=nome, email=email, telefone=telefone)
        # salva no BD
        db.session.add(nova_pessoa)
        db.session.commit()

    # retorna para a página principal
    return redirect(url_for('index'))

# inicia o servidor web
app.run(debug=True)