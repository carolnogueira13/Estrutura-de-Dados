# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

lista = []
soma = 0
multiplicacao = 1
for i in range(5):
    numero = int(input("Digite um número: "))
    soma += numero
    multiplicacao *= numero
    lista.append(numero)

print(f"Os números informados foram: {lista}")
print(f"Soma dos números: {soma}")
print(f"Multiplicação dos números: {multiplicacao}")
