# alguns imports
from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

# classe "base"
class Base(DeclarativeBase):
    pass

# classe pessoa, que herda da "base"
class Pessoa(Base):
    # nome da tabela a ser criada no banco de dados
    __tablename__ = "pessoas"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    telefone: Mapped[str] = mapped_column(String)

# definição do banco de dados
engine = create_engine("sqlite:///pessoas.db")

# configuração para criar o arquivo de banco de dados
Base.metadata.create_all(engine)

# abrir a sessão
with Session(engine) as session:

    # criar uma pessoa
    p = Pessoa(nome="João", 
               email="joao@email.com",
               telefone="11999999999")

    # adicionar a pessoa na sessão, preparando para ser gravada
    session.add(p)
        
    # confirmar a inserção no banco de dados
    session.commit()