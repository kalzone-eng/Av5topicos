import os
from datetime import date

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from pessoa import Pessoa


DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///pessoas.db")
engine = create_engine(DATABASE_URL)

pessoas = [
    Pessoa(
        nome="Ana Silva",
        email="ana@example.com",
        telefone="1111111111",
        born_date=date(1990, 1, 15),
    ),
    Pessoa(
        nome="Bruno Costa",
        email="bruno@example.com",
        telefone="2222222222",
        born_date=date(1985, 6, 20),
    ),
    Pessoa(
        nome="Carla Souza",
        email="carla@example.com",
        telefone="3333333333",
        born_date=date(1998, 11, 3),
    ),
]

with Session(engine) as session:
    session.add_all(pessoas)
    session.commit()

    for pessoa in pessoas:
        print(f"Pessoa criada: id={pessoa.id}, nome={pessoa.nome}")
