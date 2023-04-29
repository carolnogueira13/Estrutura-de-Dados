# Crie uma função de busca em que o usuário insere um valor (inteiro) e o programa retorna a sua posição na fila.

import random


def busca(fila, valor):
    corrente = fila.primeiro
    index = 1
    while corrente and corrente.dado != valor:
        corrente = corrente.proximo
        index += 1
    return corrente, index


class Nodo:
    """ Esta classe representa um nodo em uma encadeada"""

    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return "%s -> %s" % (self.dado, self.proximo)


class Fila:
    """ Esssa classe representa uma fila usando uma estrutura encadeada"""

    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __repr__(self):
        return "[" + str(self.primeiro) + "]"

    def push(self, novo_dado):
        """Inseri um elemento no final da fila"""

        novo_nodo = Nodo(novo_dado)

        if self.primeiro == None:
            self.primeiro = novo_nodo
            self.ultimo = novo_nodo
        else:
            self.ultimo.proximo = novo_nodo
            self.ultimo = novo_nodo

    def pop(self):
        """Remove o primeiro elemento da fila"""

        assert self.primeiro != None, "Impossível remover elemento de fila vazia"

        self.primeiro = self.primeiro.proximo
        if self.primeiro is None:
            self.ultimo = None


fila = Fila()

for i in range(5):
    fila.push(random.randint(0,10))

print("Fila = ", fila)

valor = int(input("Qual elemento deseja saber a posição: "))
posicao = busca(fila, valor)
if posicao[0] is not None:
    print(f"A posição do elemento {valor} é a posição {posicao[1]} da fila")