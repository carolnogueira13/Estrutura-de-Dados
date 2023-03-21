# Classe Funcionário melhorado

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def retornar_nome(self):
        return self.nome

    def retornar_salario(self):
        return self.salario

    def aumentar_salario(self, percentual):
        self.salario += self.salario * (percentual/100)


harry = Funcionario('Harry', 25000)
harry.aumentar_salario(10)
print(f"O novo salário do funcionário {harry.retornar_nome()} é R${harry.retornar_salario():.2f}")