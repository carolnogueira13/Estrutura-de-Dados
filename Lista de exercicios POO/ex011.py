# Classe Carro

class Carro:
    def __init__(self, combustivelPorLitro, tanque=0):
        self.combustivelPorLitro = combustivelPorLitro
        self.tanque = tanque

    def obter_gasolina(self):
        return self.tanque

    def andar(self, km):
        gasto = km/self.combustivelPorLitro
        self.tanque -= gasto

    def adicionar_gasolina(self, gasolina):
        self.tanque += gasolina


meuFusca = Carro(15)
meuFusca.adicionar_gasolina(20)
meuFusca.andar(100)
print(meuFusca.obter_gasolina())
