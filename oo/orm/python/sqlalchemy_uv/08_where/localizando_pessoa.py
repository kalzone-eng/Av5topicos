from sqlalchemy import create_engine, String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from typing import Optional

class Base(DeclarativeBase):
    pass

class Pessoa(Base):
    __tablename__ = "pessoas"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(250))
    email: Mapped[str] = mapped_column(String(250))
    telefone: Mapped[Optional[str]] = mapped_column(String(250), nullable=True)

engine = create_engine("sqlite:///pessoas.db")

Base.metadata.create_all(engine)

with Session(engine) as session:

    while True:
        print("1=Criar banco de dados e inserir dados exemplos")
        print("2=Buscar")
        print("3=Inserir seus dados")
        print("4=Listar todos os dados")
        print("0=Sair")

        op = input("O que você deseja fazer?")
        if op == "1":        
            p1 = Pessoa(nome="João da Silva", 
                    email="joao@email.com",
                    telefone="47 91234 5678")

            p2 = Pessoa(nome="Maria Oliveira", 
                    email="maliv@email.com",
                    telefone="47 91112222")

            p3 = Pessoa(nome="José Souza",
                        email="joso@gmail.com",
                        telefone="47 99998888")

            p4 = Pessoa(nome="Ana Paula",
                        email="ap@gmail.com",
                        telefone="47 98887777")
            
            session.add_all([p1, p2, p3, p4])
            session.commit()
            print("Banco de dados criado (se não existia), tabela criada (se não havia) e pessoa inserida no banco de dados")
            
        if op == "2":
            n = input("Qual nome deseja buscar?")

            stmt = select(Pessoa).where(Pessoa.nome.like(f"%{n}%"))
            user = session.scalars(stmt).all()
            for pessoa in user:
                print(f"Nome: {pessoa.nome}, Email: {pessoa.email}, Telefone: {pessoa.telefone}")
        
        if op == "3":
            nome = input("Digite seu nome: ")
            email = input("Digite seu email: ")
            telefone = input("Digite seu telefone: ")

            p = Pessoa(nome=nome, email=email, telefone=telefone)
            session.add(p)
            session.commit()
            print("Pessoa inserida no banco de dados")
            
        if op == "4":
            stmt = select(Pessoa)
            pessoas = session.scalars(stmt).all()
            for pessoa in pessoas:
                print(f"Nome: {pessoa.nome}, Email: {pessoa.email}, Telefone: {pessoa.telefone}")
            
        if op == "0":
            break