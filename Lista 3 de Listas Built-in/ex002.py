# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

import random
lista = []
for i in range(1,11):
    lista.append(random.randrange(10))
print("A lista direta é: ", end="")
for e in lista:
    print(e, end=" ")

print("\nA lista invertida é: ", end="")
for e in range(-1, -(len(lista) + 1), -1):
    print(lista[e], end=" ")

lista.reverse()
print("\nA lista invertida é: ", end="")
for e in lista:
    print(e, end=" ")
    

    