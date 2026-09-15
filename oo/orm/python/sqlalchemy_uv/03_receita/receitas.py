from sqlalchemy import create_engine, String, Text, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from typing import Optional

class Base(DeclarativeBase):
    pass

class Receita(Base):
    __tablename__ = "tabela_receitas"
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(250))
    tempo_preparo: Mapped[int] = mapped_column(Integer)
    modo_preparo: Mapped[str] = mapped_column(Text)
    ingredientes: Mapped[str] = mapped_column(Text)

engine = create_engine("mysql+pymysql://root:root@localhost:3306/meubanco")

Base.metadata.create_all(engine)

with Session(engine) as session:

  r1 = Receita(nome = "Bolo de milho", tempo_preparo = 50,

      modo_preparo = "Bate no liquidificador a farinha, o milho, "+\
      "o leite, óleo e os ovos, até moer bem "+\
      "o milho. Acrescente o fermento e "+\
      "pulse o liquidificador 3 vezes. "+\
      "Despeje na forma e leve a forno"+\
      " por 50 minutos. Espere esfriar e sirva.",

      ingredientes = "1 lata de milho,  leite (medida da lata), " +\
      "açúcar (medida da lata), 3 ovos, 1 colher de fermento," +\
      "1/2 lata de óleo"
  )

  session.add(r1)
  session.commit()

  print("A tabela foi criada (se não existia) e os dados da receita foram inseridos.")
  print(f"A receita chamada {r1.nome} foi salva sob o número {r1.id}.")