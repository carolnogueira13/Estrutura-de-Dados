# Escreva um método para remover elementos repetidos de uma pilha

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

    def remove_duplicadas(self):
        # Conjunto para armazenar valores únicos
        valores_unicos = set()

        # Inicializa variaveis para percorrer a lista
        ant = None
        corrente = self.topo

        # Percorre a pilha
        while corrente:
            # Verifica se o valor está no set
            if corrente.dado in valores_unicos:
                # Remove o nodo atual da pilha
                ant.anterior = corrente.anterior
            else:
                # Adiciona o valor ao conjunto
                valores_unicos.add(corrente.dado)
                ant = corrente
            corrente = corrente.anterior


pilha = Pilha()
pilha.insere(1)
pilha.insere(5)
pilha.insere(1)
pilha.insere(6)
pilha.insere(5)
print(f"Pilha original: {pilha}")
pilha.remove_duplicadas()
print(f"Pilha com elementos duplicados removidos: {pilha}")
