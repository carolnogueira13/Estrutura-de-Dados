# Escrever uma função que receba como parâmetro uma pilha. A função deve retornar o maior elemento da pilha.

def maior(pilha):
    corrente = pilha.topo
    maior = corrente.dado
    while corrente:
        if corrente.dado > maior:
            maior = corrente.dado
        corrente = corrente.anterior
    return maior


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
        """Inseri um elemento no topo da pilha"""
        novo_nodo = Nodo(novo_dado)
        novo_nodo.anterior = self.topo
        self.topo = novo_nodo

    def remove(self):
        """Remove o elemento que está no topo da pilha"""
        assert self.topo, "Impossível remover valor da pilha vazia"
        self.topo = self.topo.anterior


pilha = Pilha()
pilha.insere(9)
pilha.insere(10)
pilha.insere(56)
pilha.insere(6)
print("Pilha: ", pilha)
print("O maior elemento da pilha é: ", maior(pilha))


