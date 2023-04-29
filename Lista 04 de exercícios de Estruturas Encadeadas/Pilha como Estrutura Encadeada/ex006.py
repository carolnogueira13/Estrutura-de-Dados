# Escreva uma função chamada TPilha2 que recebe como parâmetro 2 pilhas (N e P) e um vetor de inteiros. Para cada um:
#
# se positivo, inserir na pilha P;
# se negativo, inserir na pilha N;
# se zero, retirar um elemento de cada pilha.

import random


def TPilha2(P, N, lista):
    for i in lista:
        if i > 0:
            P.insere(i)
        elif i < 0:
            N.insere(i)
        if N.topo is not None and i == 0:
            N.remove()
        if P.topo is not None and i == 0:
            P.remove()


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
    lista.append(random.randint(-9,10))
print("Lista: ", lista)
pilha1 = Pilha()
pilha2 = Pilha()
TPilha2(pilha1, pilha2, lista)
print("Pilha 1 (positivos) = ", pilha1)
print("Pilha 2 (negativos) = ", pilha2)