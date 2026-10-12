from config import *
from models.aviao import Aviao
import services.avioes as aviao_service


@app.route('/avioes', methods=['GET'])
def retornar_avioes():

    avioes = aviao_service.retornar_avioes()

    return jsonify({
        "resultado": "ok",
        "detalhes": [aviao.json() for aviao in avioes]
    })



@app.route('/aviao', methods=['POST'])
@jwt_required()
def criar_aviao():

    dados = request.json

    if (not dados
        or not dados.get('modelo')
        or not dados.get('piloto')
        or not dados.get('copiloto')
        or not dados.get('passageiros')
        or not dados.get('companhia')
    ):
        return jsonify({
            "resultado": "erro",
            "detalhes": "Modelo, piloto, copiloto, passageiros e companhia aérea são obrigatórios"
        }), 400

    aviao = aviao_service.criar_aviao(dados)

    return jsonify({
        "resultado": "ok",
        "detalhes": aviao.json()
    }), 201
