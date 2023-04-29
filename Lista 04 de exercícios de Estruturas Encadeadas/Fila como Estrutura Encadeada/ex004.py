# Escreva uma função que inverta a ordem dos elementos da fila.
import random


def inverte(fila):
    corrente = fila.primeiro
    lista = []
    while corrente:
        lista.append(corrente.dado)
        corrente = corrente.proximo
    fila2 = Fila()
    for termo in range(len(lista)):
        fila2.push(lista.pop())
    return fila2


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

        if self.primeiro is None:
            self.primeiro = novo_nodo
            self.ultimo = novo_nodo
        else:
            self.ultimo.proximo = novo_nodo
            self.ultimo = novo_nodo

    def pop(self):
        """Remove o primeiro elemento da fila"""

        assert self.primeiro is not None, "Impossível remover elemento de fila vazia"

        self.primeiro = self.primeiro.proximo
        if self.primeiro is None:
            self.ultimo = None


fila = Fila()
for i in range(9):
    fila.push(random.randint(0,10))
print("Fila: ", fila)
fila_invertida = inverte(fila)
print("Fila invertida: ", fila_invertida)
