# Implemente uma fila dinâmica contendo todas as funcionalidades de uma fila padrão. Para isso, resolvar:
# –Crie um nó padrão da fila.
# –Crie uma função de inicialização da fila vazia
# –Crie uma função push que cria e insere um novo nó para o final da fila.
# –Crie uma função pop que remove o primeiro elemento da fila.

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
print("Fila vazia: ", fila)

for i in range(5):
    fila.push(i)
    print(f"Inseri o valor {i} no final da fila {fila}")

while fila.primeiro is not None:
    fila.pop()
    print("Removendo o elemento que está no começo da fila: ", fila)
