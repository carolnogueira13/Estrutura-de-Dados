# Classe bichinho virtual++

class Bichinho:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def __str__(self):
        return f"Atributos do bichinho: Nome: {self.nome} Fome: {self.fome} Saúde: {self.saude} Idade: {self.idade}"

    def retornar_nome(self):
        return self.nome

    def retornar_fome(self):
        return self.fome

    def retornar_saude(self):
        return self.saude

    def retornar_idade(self):
        return self.idade

    def alterar_nome(self, novoNome):
        self.nome = novoNome

    def alterar_fome(self, comida):
        self.fome += comida/2

    def alterar_saude(self, novoSaude):
        self.saude = novoSaude

    def alterar_idade(self, novoidade):
        self.idade = novoidade

    def retornar_humor(self, tempoDeBrincar=0):
        humor = self.saude / 2 + self.fome / 2
        humor += tempoDeBrincar/5
        return humor


bichinho = Bichinho("Pipoca", 2, 4, 11)
bichinho.AlterarFome(2)
print(bichinho)