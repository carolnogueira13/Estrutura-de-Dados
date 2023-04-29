# Escreva uma função que receba como parâmetro duas pilhas e verifique de elas são iguais.
# Duas pilhas são iguais se possuem os mesmos elementos, na mesma ordem.

def comparacao(pilha1, pilha2):
    corrente1 = pilha1.topo
    corrente2 = pilha2.topo
    while corrente1 and corrente2:
        if corrente1.dado != corrente2.dado:
            return "Pilhas diferentes"
        corrente1 = corrente1.anterior
        corrente2 = corrente2.anterior
    if corrente1 is None and corrente2 is None:
        return "Pilhas iguais"
    else:
        return "Pilhas diferentes"


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
        """Inseri um elemento no final da pilha"""
        novo_nodo = Nodo(novo_dado)
        novo_nodo.anterior = self.topo
        self.topo = novo_nodo

    def remove(self):
        """Remove o elemento que está no topo da pilha"""
        assert self.topo, "Impossível remover valor da pilha vazia"
        self.topo = self.topo.anterior


pilha1 = Pilha()
pilha2 = Pilha()
pilha3 = Pilha()
for i in range(8):
    pilha1.insere(i)
    pilha2.insere(i)
for i in range(9):
    pilha3.insere(i)

print("Pilha 1: ", pilha1)
print("Pilha 2: ", pilha2)
print("Pilha 3: ", pilha3)
print("Comparação pilha 1 e pilha 2: ", comparacao(pilha1, pilha2))
print("Comparação pilha 2 e pilha 3: ", comparacao(pilha2, pilha3))