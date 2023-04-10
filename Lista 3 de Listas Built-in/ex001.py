# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os
import random

lista = []
for i in range(5):
    lista.append(random.randrange(10))
print("A lista é: ", end="")
for e in lista:
    print(e, end=" ")
