from datetime import date

from sqlalchemy import Date, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Pessoa(Base):
    __tablename__ = "tabela_pessoa"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(250))
    email: Mapped[str] = mapped_column(String(250))
    telefone: Mapped[str] = mapped_column(String(250))
    born_date: Mapped[date | None] = mapped_column(Date, nullable=True)
