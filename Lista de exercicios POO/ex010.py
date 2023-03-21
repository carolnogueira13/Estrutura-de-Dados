# Classe bomba de combustivel

class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def alterar_valor(self, valor):
        self.valorLitro = valor

    def alterar_combustivel(self, combustivel):
        self.tipoCombustivel = combustivel

    def alterar_quantidade_combustivel(self, quant):
        self.quantidadeCombustivel = quant

    def abastercer_por_valor(self, valor):
        quant = valor/self.valorLitro
        self.quantidadeCombustivel += quant
        return quant

    def abastecer_por_litros(self, litros):
        self.quantidadeCombustivel += litros
        return litros/self.valorLitro

