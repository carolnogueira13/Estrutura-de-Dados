# Classe Bola

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def mostra_cor(self):  # get
        return self.cor

    def troca_cor(self, novacor):  # set
        self.cor = novacor

