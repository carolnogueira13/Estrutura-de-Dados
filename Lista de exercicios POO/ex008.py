# Classe Macaco

class Macaco:
    def __init__(self, nome, estomago=[]):
        self.nome = nome
        self.estomago = estomago

    def comer(self, comida):
        self.estomago.append(comida)

    def ver_bucho(self):
        return self.estomago

    def digerir(self, comida):
        self.estomago.remove(comida)


macaco1 = Macaco('Felix')
macaco1.comer("banana")
print(macaco1.ver_bucho())
macaco1.comer("maçã")
print(macaco1.ver_bucho())
macaco1.digerir("maçã")
print(macaco1.ver_bucho())
macaco1.comer("chocolate")
print(macaco1.ver_bucho())
macaco1.digerir("chocolate")
print(macaco1.ver_bucho())

macaco2 = Macaco('Xiita', ['laranja'])
print(macaco2.ver_bucho())
macaco2.comer(macaco1)
print(macaco2.ver_bucho())
macaco2.digerir(macaco1)
print(macaco2.ver_bucho())
macaco2.comer("Melancia")
print(macaco2.ver_bucho())
