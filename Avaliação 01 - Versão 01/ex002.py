# Escreva um método em Python para remover elementos cujos valores estão em um range específico em uma lista Encadeada

class NodoLista:
    """ Esta classe representa um nodo de uma lista encadeada"""

    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo_nodo = proximo_nodo

    def __repr__(self):
        return "%s -> %s" % (self.dado, self.proximo_nodo)


class ListaEncadeada:
    """Esta classe representa uma lista encadeado"""

    def __init__(self):
        self.cabeca = None

    def __repr__(self):
        return "[" + str(self.cabeca) + "]"

    def insere_no_inicio(self, novo_dado):
        novo_nodo = NodoLista(novo_dado)
        novo_nodo.proximo_nodo = self.cabeca
        self.cabeca = novo_nodo

    def busca(self, anterior, nodo, valor, valor2):
        anterior = anterior
        corrente = nodo
        while corrente and not(valor <= corrente.dado <= valor2):
            anterior = corrente
            corrente = corrente.proximo_nodo
        return anterior, corrente

    def remove(self, valor, valor2):
        assert self.cabeca, "Inpossível remover valor de lista vazia."

        corrente = self.cabeca
        anterior = None
        while True and corrente:
            nodo_a_remover = self.busca(anterior, corrente, valor, valor2)
            if not nodo_a_remover[1]:
                break
            if nodo_a_remover[1] == self.cabeca:
                self.cabeca = nodo_a_remover[1].proximo_nodo
            else:
                nodo_a_remover[0].proximo_nodo = nodo_a_remover[1].proximo_nodo
            anterior = corrente
            corrente = corrente.proximo_nodo


lista = ListaEncadeada()
lista.insere_no_inicio(2)
lista.insere_no_inicio(3)
lista.insere_no_inicio(4)
lista.insere_no_inicio(5)
lista.insere_no_inicio(3.3)
print(f"Lista original: {lista}")
inicio = 3
fim = 5.8
lista.remove(inicio, fim)
print(f"Lista depois da remoção de elementos do intervalo [{inicio},{fim}]: {lista}")

