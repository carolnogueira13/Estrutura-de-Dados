# Classe Pessoa

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, nova_idade):
        if nova_idade > self.idade:
            if self.idade < 21:
                for i in range(self.idade, nova_idade):
                    if i == 21:
                        break
                    self.altura += 0.05
                self.crescer(self.altura)
            self.idade = nova_idade

    def engordar(self, novo_peso):
        if novo_peso > self.peso:
            self.peso = novo_peso

    def emagrecer(self, novo_peso):
        if novo_peso < self.peso:
            self.peso = novo_peso

    def crescer(self, nova_altura):
        if nova_altura > self.altura:
            self.altura = nova_altura
