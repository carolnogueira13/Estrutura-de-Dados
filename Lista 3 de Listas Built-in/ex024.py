# Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor .
# Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para
# gerar numeros aleatórios, simulando os lançamentos dos dados.

import random


def porcentagem(parte, total):
    return (100 * parte) / total


# Lista dos 100 lançaementos
lancamentos = []
for i in range(100):
    lancamentos.append(random.randint(1, 6))

# Lista da porcentagem de cada tipo de lançamento
porcentagens = []
for i in range(1, 7):
    porcentagens.append(porcentagem(lancamentos.count(i), len(lancamentos)))

print(f"\n{'Valor':<20}{'Nº de Lançamentos':<20}{'Porcentagem'}")
for i, por in enumerate(porcentagens):
    print(f"{i + 1:<20} {lancamentos.count(i + 1):<20} {por:<10.2f}%")
print(f"\nNº de Lançamentos totais: {len(lancamentos)}")
