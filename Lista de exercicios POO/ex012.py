# Classe Conta de Investimento


class Conta:
    def __init__(self, numero, nome, saldo=0):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor


class ContaInvestimento(Conta):
    def __init__(self, numero, nome, saldo=0.0, taxaJuros=0.0):
        super().__init__(numero, nome, saldo)
        self.taxaJuros = taxaJuros

    def adicione_juros(self):
        self.saldo += self.saldo * (self.taxaJuros / 100)


conta2 = ContaInvestimento(1233, 'ana', 1000, 10)
conta2.adicione_juros()
conta2.adicione_juros()
conta2.adicione_juros()
conta2.adicione_juros()
conta2.adicione_juros()
print(f"O novo saldo da conta é {conta2.saldo}")
