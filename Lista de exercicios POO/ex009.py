# Classe ponto e retãngulo

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def retornar_x(self):
        return self.x

    def retornar_y(self):
        return self.y


class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def centro_x(self):
        x = self.largura / 2
        return x

    def centro_y(self):
        y = self.altura / 2
        return y


while True:
    larg = float(input("Insira o largura do retâgulo:"))
    alt = float(input("Inisra a altura do retângulo:"))
    retangulo1 = Retangulo(larg, alt)
    centro_ret01 = Ponto(retangulo1.centro_x(), retangulo1.centro_y())
    print(f"O centro do retângulo é ({centro_ret01.retornar_x()},{centro_ret01.retornar_y()})")
    resp = str(input("Deseja inserir os valores de mais um retâgulo [S/N] : ")).upper().strip()
    if resp == "N":
        break
