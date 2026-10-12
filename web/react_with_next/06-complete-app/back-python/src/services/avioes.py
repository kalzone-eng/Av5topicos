from config import *
from models.aviao import Aviao


def criar_aviao(data):
    aviao = Aviao(
        modelo=data['modelo'],
        piloto=data['piloto'],
        copiloto=data['copiloto'],
        passageiros=data['passageiros'],
        companhia=data['companhia']
    )

    db.session.add(aviao)
    db.session.commit()

    return aviao


def retornar_avioes():
    avioes = Aviao.query.all()

    return avioes
