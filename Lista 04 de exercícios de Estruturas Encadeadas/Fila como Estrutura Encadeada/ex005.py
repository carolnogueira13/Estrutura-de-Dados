# Fila dos processos do gerenciador de tarefas

class Process:
    def __init__(self, id, name, priority, wait):
        self.id = id
        self.name = name
        self.priority = priority
        self.wait = wait

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, priority: {self.priority}, wait: {self.wait}"


class Nodo:
    """ Esta classe representa um nodo em uma encadeada"""

    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return "%s -> %s" % (self.dado, self.proximo)


class FilaDeProcesso:
    """ Esssa classe representa uma fila usando uma estrutura encadeada"""

    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __repr__(self):
        corrente = self.primeiro
        resp = ""
        i = 1
        while corrente:
            resp += f"Processo {i}: " + "{" + f"{corrente.dado}" + "} "
            corrente = corrente.proximo
            i += 1
        return resp

    def insere_processo(self, novo_dado):
        """Inseri um processo na fila"""

        novo_nodo = Nodo(novo_dado)

        if self.primeiro is None:
            self.primeiro = novo_nodo
            self.ultimo = novo_nodo
        else:
            self.ultimo.proximo = novo_nodo
            self.ultimo = novo_nodo

    def busca(self, valor):
        corrente = self.primeiro
        anterior = None
        while corrente and corrente.dado.wait != valor:
            anterior = corrente
            corrente = corrente.proximo
        return anterior, corrente

    def matar_processo(self):
        """ Matar o processo com maior tempo de espera"""

        assert self.primeiro, "Inpossível remover valor de lista vazia."

        corrente = self.primeiro
        maior = corrente.dado.wait
        while corrente:
            if corrente.dado.wait > maior:
                maior = corrente.dado.wait
            corrente = corrente.proximo

        nodo_a_remover = self.busca(maior)
        if not nodo_a_remover[1]:
            return

        if nodo_a_remover[1] == self.primeiro:
            self.primeiro = nodo_a_remover[1].proximo
        else:
            nodo_a_remover[0].proximo = nodo_a_remover[1].proximo

    def executar_processo(self):
        """Remove o primeiro processo da fila"""

        assert self.primeiro is not None, "Impossível remover elemento de fila vazia"

        self.primeiro = self.primeiro.proximo
        if self.primeiro is None:
            self.ultimo = None


fila = FilaDeProcesso()
fila.insere_processo(Process(100, "Word", 3, 10))
fila.insere_processo(Process(101, "Excel", 3, 13))
fila.insere_processo(Process(102, "Chrome", 3, 17))
fila.insere_processo(Process(103, "Pycharm", 3, 30))
fila.insere_processo(Process(104, "Power Point", 3, 19))
print("Fila inicial: ", fila)
fila.matar_processo()
print("Fila após matar o proceeso de maior tempo de espera: ", fila)
fila.executar_processo()
print("Fila após executar o primeiro processo: ", fila)
