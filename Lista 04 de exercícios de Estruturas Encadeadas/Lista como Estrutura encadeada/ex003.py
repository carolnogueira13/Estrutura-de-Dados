# Defina as funções inserção, remoção e busca como métodos da Classe Lista.

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

    def insere_depois(self, nodo_anterior, novo_dado):
        assert nodo_anterior, "Nodo anterior precisa existir na lista."

        novo_nodo = NodoLista(novo_dado)
        novo_nodo.proximo_nodo = nodo_anterior.proximo_nodo
        nodo_anterior.proximo_nodo = novo_nodo

    def busca(self, valor):  # Buscar o valor em uma lista
        corrente = self.cabeca
        anterior = None
        while corrente and corrente.dado != valor:
            anterior = corrente
            corrente = corrente.proximo_nodo
        return anterior, corrente

    def remove(self, valor):
        assert self.cabeca, "Inpossível remover valor de lista vazia."

        nodo_a_remover = self.busca(valor)
        if not nodo_a_remover[1]:
            return

        if nodo_a_remover[1] == self.cabeca:
            lista.cabeca = nodo_a_remover[1].proximo_nodo
        else:
            nodo_a_remover[0].proximo_nodo = nodo_a_remover[1].proximo_nodo


lista = ListaEncadeada()
lista.insere_no_inicio(2)
lista.insere_no_inicio(3)
lista.insere_depois(lista.cabeca, 4)
print("Lista: ", lista)
lista.remove(4)
print("Lista depois da remoção do 4: ", lista)

