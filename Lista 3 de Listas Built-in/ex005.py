# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os
# números IMPARES no vetor impar. Imprima os três vetores.

lista = []
pares = []
impares = []

for i in range(20):
    lista.append(int(input(f"Informe o {i + 1}º número: ")))

print("Todos os números:", end=" ")
for numero in lista:
    print(numero, end=" ")
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("\nNúmeros pares:", end=" ")
for numero in pares:
    print(numero, end=" ")

print("\nNúmeros ímpares:", end=" ")
for numero in impares:
    print(numero, end=" ")

