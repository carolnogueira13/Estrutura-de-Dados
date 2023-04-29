# Implemente uma função chamada TPilha, que receba um vetor de inteiros com 15 elementos.
# Para cada um deles, como segue:
#
# Se o número for par, insira-o na pilha;
# Se o número lido for ímpar, retire um número da pilha;
# Ao final, esvazie a pilha imprimindo os elementos.

import random


def TPilha(lista):
    pilha = Pilha()
    for i in lista:
        if i % 2 == 0:
            pilha.insere(i)
        if pilha.topo is not None and i % 2 != 0:
            pilha.remove()
    print("Pilha formada: ", end=" ")
    while pilha.topo:
        print(pilha.topo.dado, end=" ")
        pilha.remove()


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


lista = []
for i in range(15):
    lista.append(random.randrange(10))
print("Lista: ", lista)
TPilha(lista)
