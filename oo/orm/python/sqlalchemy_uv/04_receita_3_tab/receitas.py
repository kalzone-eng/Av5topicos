from sqlalchemy import create_engine, String, Text, Integer, Float, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from typing import List, Optional

class Base(DeclarativeBase):
    pass

class Receita(Base):
    __tablename__ = "tabela_receitas"
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(250))
    tempo_preparo: Mapped[int] = mapped_column(Integer)
    modo_preparo: Mapped[str] = mapped_column(Text)

    ingredientes: Mapped[List["IngredienteNaReceita"]] = relationship(back_populates="receita")

'''
a Receita tem uma lista de objetos IngredienteNaReceita. 
Mas para o SQLAlchemy saber como montar essa lista automaticamente, 
ele precisa saber qual é o "outro lado" dessa relação, 
ou seja, qual atributo, dentro de IngredienteNaReceita, 
aponta "de volta" para a Receita.
Esse "outro lado" é o back_populates.'''
   

class Ingrediente(Base):
    __tablename__ = "tabela_ingredientes"
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(250))

    # lista reversa
    receitas: Mapped[List["IngredienteNaReceita"]] = relationship(back_populates="ingrediente")

class IngredienteNaReceita(Base):
    __tablename__ = "tabela_ingrediente_na_receita"

    # chave estrangeira
    ingrediente_id: Mapped[int] = mapped_column(
        ForeignKey("tabela_ingredientes.id"), 
        primary_key=True)

    # chave estrangeira
    receita_id: Mapped[int] = mapped_column(
        ForeignKey("tabela_receitas.id"), 
        primary_key=True)

    # atributos de acesso ao objeto
    # (acima só temos o "id", nesses atributos 
    # abaixo conseguimos ter acesso ao objeto "inteiro")
    ingrediente: Mapped["Ingrediente"] = relationship(
        back_populates="receitas")    
    receita: Mapped["Receita"] = relationship(
        back_populates="ingredientes")    

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

  ir1 = IngredienteNaReceita(ingrediente = i1, 
                             receita = r1, 
                             quantidade=1, 
                             unidade="lata de milho")

  ir2 = IngredienteNaReceita(ingrediente = i2, 
                               receita = r1, 
                               quantidade=1, 
                               unidade="lata de milho")
  
  ir3 = IngredienteNaReceita(ingrediente = i3, 
                               receita = r1, 
                               quantidade=1, 
                               unidade="lata de milho")
  
  ir4 = IngredienteNaReceita(ingrediente = i4, 
                             receita = r1, 
                             quantidade=3, 
                             unidade="ovo")

  ir5 = IngredienteNaReceita(ingrediente = i5, 
                               receita = r1, 
                               quantidade=1, 
                               unidade="colher de café")

  ir6 = IngredienteNaReceita(ingrediente = i6, 
                               receita = r1, 
                               quantidade=0.5, 
                               unidade="lata de milho")

  # podemos adicionar apenas a receita, que já contém 
  # todos os outros objetos
  session.add(r1)

  # salvar tudo!
  session.commit()

  print("A tabela foi criada (se não existia) e os dados da receita foram inseridos.")
  print(f"A receita chamada {r1.nome} foi salva sob o número {r1.id}.")

  print("Ingredientes da receita:")
  for item in r1.ingredientes:
    print(item.ingrediente.nome, item.quantidade, item.unidade)