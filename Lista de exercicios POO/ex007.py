# Classe bichinho virtual

class Bichinho:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def retornar_nome(self):
        return self.nome

    def retornar_fome(self):
        return self.fome

    def retornar_saude(self):
        return self.saude

    def retornar_idade(self):
        return self.idade

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def alterar_fome(self, novo_fome):
        self.fome = novo_fome

    def alterar_saude(self, novo_saude):
        self.saude = novo_saude

    def alterar_idade(self, novo_dade):
        self.idade = novo_dade

    def retornar_humor(self):
        return self.saude/2 + self.fome/2


