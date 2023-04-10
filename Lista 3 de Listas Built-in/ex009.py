# Faça um Programa que leia um vetor A com 10 números inteiros,
# calcule e mostre a soma dos quadrados dos elementos do vetor.

lista = []
soma = 0
for i in range(10):
    numero = int(input("Digite um número: "))
    soma += (numero * numero)
    lista.append(numero)

print(f"Os números informados foram: {lista}")
print(f"Soma dos quadrados dos números informados é: {soma}")