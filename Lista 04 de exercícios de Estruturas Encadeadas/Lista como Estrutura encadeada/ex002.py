# Remova duplicatas de uma lista ordenada. Suponha que lhe seja fornecida uma lista encadeada armazenando
# números inteiros em ordem crescente. Sua tarefa é remover todos os elementos duplicados da
# lista. Por exemplo, dada a lista [0 → 1 → 1 → 5 → 7 → 10 → 10 → None],
# seu programa deve retornar a lista [0 → 1 → 5 → 7 → 10 → None].

def remove_duplicadas(lista):
    corrente = lista.cabeca
    while corrente:
        proximo_distinto = corrente.proximo_nodo
        while proximo_distinto and proximo_distinto.dado == corrente.dado:
            proximo_distinto = proximo_distinto.proximo_nodo
        corrente.proximo_nodo = proximo_distinto
        corrente = proximo_distinto
    return lista


def insere_no_inicio(lista, novo_dado):
    novo_nodo = NodoLista(novo_dado)
    novo_nodo.proximo_nodo = lista.cabeca
    lista.cabeca = novo_nodo


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
insere_no_inicio(lista, 10)
insere_no_inicio(lista, 10)
insere_no_inicio(lista, 7)
insere_no_inicio(lista, 5)
insere_no_inicio(lista, 1)
insere_no_inicio(lista, 1)
insere_no_inicio(lista, 0)
print("Lista com elementos repetidos: ", lista)
remove_duplicadas(lista)
print("Lista sem elementos duplicados: ", lista)
