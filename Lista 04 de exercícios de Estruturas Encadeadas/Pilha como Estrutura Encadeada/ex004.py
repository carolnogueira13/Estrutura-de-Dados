# Pilha para o problema com os carros

class Nodo:
    """ Esta classe representa um nodo em uma encadeada"""

    def __init__(self, dado=0, nodo_anterior=None):
        self.dado = dado
        self.anterior = nodo_anterior

    def __repr__(self):
        return "%s -> %s" % (self.dado, self.anterior)


class Pilha:
    """ Esssa classe representa uma pilha usando uma estrutura encadeada"""

    def __init__(self):
        self.topo = None

    def __repr__(self):
        return "[" + str(self.topo) + "]"

    def insere(self, novo_dado):
        novo_nodo = Nodo(novo_dado)
        novo_nodo.anterior = self.topo
        self.topo = novo_nodo

    def remove(self):
        assert self.topo, "Impossível remover valor da pilha vazia"
        self.topo = self.topo.anterior

    def busca(self, valor):
        corrente = self.topo
        while corrente and corrente.dado != valor:
            corrente = corrente.anterior
        return corrente

    def removidos(self, valor):
        corrente = self.topo
        while True:
            if corrente.dado != valor:
                print(corrente.dado, end=" ")
            if corrente.dado == valor:
                break
            corrente = corrente.anterior


pilha = Pilha()
while True:
    pilha.insere(int(input("Carro: ")))
    resp = input("Deseja inserir mais um carro: ").upper()[0]
    if resp == "N":
        break
print("Lista de carros: ", pilha)
carro = int(input("Qual carro deseja remover: "))
if pilha.busca(carro):
    print(f"O carro {carro} está estacionado na rua e para remove-lo precisa retirar os carros:", end = " ")
    pilha.removidos(carro)
else:
    print(f"O carro {carro} não está estacionado na rua")
