from config import *
class Aviao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(200), nullable=False)
    piloto = db.Column(db.String(200), nullable=False)
    copiloto = db.Column(db.String(200), nullable=True)
    passageiros = db.Column(db.String(200), nullable=False)
    companhia = db.Column(db.String(200), nullable=False)

    def json(self):
        return {
            "id":self.id,
            "modelo":self.modelo,
            "piloto":self.piloto,
            "copiloto":self.copiloto,
            "passageiros":self.passageiros,
            "companhia":self.companhia
            }
