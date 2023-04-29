# Implemente a função remove utilizando a função busca

def insere_no_inicio(lista, novo_dado):
    novo_nodo = NodoLista(novo_dado)
    novo_nodo.proximo_nodo = lista.cabeca
    lista.cabeca = novo_nodo


def insere_depois(lista, nodo_anterior, novo_dado):
    assert nodo_anterior, "Nodo anterior precisa exixtir na lista."

    novo_nodo = NodoLista(novo_dado)
    novo_nodo.proximo_nodo = nodo_anterior.proximo_nodo
    nodo_anterior.proximo_nodo = novo_nodo


def busca(lista, valor):
    corrente = lista.cabeca
    anterior = None
    while corrente and corrente.dado != valor:
        anterior = corrente
        corrente = corrente.proximo_nodo
    return anterior, corrente


def remove(lista, valor):
    assert lista.cabeca, "Impossível remover valor de lista vazia."

    nodo_a_remover = busca(lista, valor)
    if not nodo_a_remover[1]:
        return

    if nodo_a_remover[1] == lista.cabeca:
        lista.cabeca = nodo_a_remover[1].proximo_nodo
    else:
        nodo_a_remover[0].proximo_nodo = nodo_a_remover[1].proximo_nodo


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


lista = ListaEncadeada()
for i in range(7):
    insere_no_inicio(lista, i)
print("Lista: ", lista)

print("Removendo elementos:")
for i in range(7):
    remove(lista, i)
    print(f"Removendo o elemento {i}: {lista}")
