from sqlalchemy import create_engine, String, Text, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship, List
from typing import Optional

class Base(DeclarativeBase):
    pass

class Receita(Base):
    __tablename__ = "tabela_receitas"
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(250))
    tempo_preparo: Mapped[int] = mapped_column(Integer)
    modo_preparo: Mapped[str] = mapped_column(Text)
    ingredientes: Mapped[List["Ingrediente"]] = relationship(back_populates="pessoa")

class Ingrediente(Base):
    __tablename__ = "tabela_ingredientes"
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(250))
    ingredientes: Mapped[List["Ingrediente"]] = relationship(back_populates="pessoa")

class IngredienteNaReceita(Base):
    __tablename__ = "tabela_ingrediente_na_receita"
    ingrediente_id: Mapped[int] = mapped_column(ForeignKey("tabela_ingredientes.id"))
    ingrediente: Mapped["Ingrediente"] = relationship(back_populates="ingredientes")    
    receita_id: Mapped[int] = mapped_column(ForeignKey("tabela_receitas.id"))
    receita: Mapped["Receita"] = relationship(back_populates="receitas")    
    unidade: Mapped[str] = mapped_column(String(250))
    quantidade: Mapped[float] = mapped_column(Float())
    
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
   )
  i1 = Ingrediente(nome = "milho")
  i2 = Ingrediente(nome = "leite")
  i3 = Ingrediente(nome = "açúcar")
  i4 = Ingrediente(nome = "ovo")
  i5 = Ingrediente(nome = "fermento")
  i6 = Ingrediente(nome = "óleo")

  r1.ingredientes.add(i1)
  r1.ingredientes.add(i2)
  r1.ingredientes.add(i3)
  r1.ingredientes.add(i4)
  r1.ingredientes.add(i5)
  r1.ingredientes.add(i6)


  r2 = Receita(nome = "Tapioca com ovo e leite (crepioca)", tempo_preparo = 10,
  
        modo_preparo = '''
a) Em uma tigela, misture bastante a tapioca com o leite; 
b) adicione os ovos, o açúcar e o sal e mexa bem; 
c) deixe a massa descansar por 10 minutos; 
d) aqueça uma frigideira antiaderente; 
e) despeje e espalhe uma concha da massa na frigideira; 
f) cozinhe por 3 minutos; 
g) vire a tapioca e cozinhe mais 2 minutos; 
h) retire da frigideira e repita o processo 
com o restante da massa.
'''
     )
 
  r2.ingredientes.add(i1)
  
  

  session.add(r1)
  session.commit()

  print("A tabela foi criada (se não existia) e os dados da receita foram inseridos.")
  print(f"A receita chamada {r1.nome} foi salva sob o número {r1.id}.")