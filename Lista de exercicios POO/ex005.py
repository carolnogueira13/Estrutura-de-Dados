# Classe Conta-corrente

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


conta = Conta(1234, 'jose', 200)
conta.deposito(1000)
conta.saque(200)
print(f"A saldo da conta é {conta.saldo}")
