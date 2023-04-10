# 17) Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
# O resultado do atleta será determinado pela média dos cinco valores restantes.
# Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e
# depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando
# não for informado o nome do atleta.

import numpy as np

nomes = []
saltos = []

while True:
    nome = str(input("Atleta: "))
    if nome == "":
        break
    nomes.append(nome)
    saltos.append(float(input("Primeiro Salto:")))
    saltos.append(float(input("Segundo Salto:")))
    saltos.append(float(input("Terceiro Salto:")))
    saltos.append(float(input("Quarto Salto:")))
    saltos.append(float(input("Quinto Salto:")))

print("Resultado final: ")
print(f"Atleta: {nomes[0]}")
print(f"Saltos: ", end="")
for i, salto in enumerate(saltos):
    if i != (len(saltos)-1):
        print(f"{salto} - ", end="")
    else:
        print(salto)
print(f"Média dos saltos: {np.mean(saltos)} m")