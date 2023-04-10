# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos
# possuem altura inferior à média de altura desses alunos.

# Duas formas:

# 1ª forma (sem pandas e somente com listas):

'''Leitura da idade e altura dos alunos:
alunos = [[] for i in range(30)]
for i in range(30):
    alunos[i].append(int(input(f"Digite a idade da {i+1}ª pessoa: "))
    alunos[i].append(float(input(f"Digite a altura da {i+1}ª pessoa: ")))'''

alunos = [[21, 1.8],[22, 1.8],[23, 1.7],[24, 1.8],[25, 1.7],[26, 1.8],[27, 1.7],[28, 1.8],[29, 1.8],[30, 1.8],[21, 1.8],
          [22, 1.8],[23, 1.7],[24, 1.8],[25, 1.7],[26, 1.8],[27, 1.7],[28, 1.8],[29, 1.8],[30, 1.8],[21, 1.8],[22, 1.8],
          [23, 1.7],[24, 1.8],[25, 1.7],[26, 1.8],[27, 1.7],[28, 1.8],[29, 1.8], [30, 1.8]]

soma_de_altura = media_de_altura = alunos_procurados = 0

for i, termo in enumerate(alunos):
    soma_de_altura += termo[1]

media_de_altura = soma_de_altura/30

for i, termo in enumerate(alunos):
    if termo[0] >= 13 and termo[1] <= media_de_altura:
        alunos_procurados += 1

print(f"O número de alunos maiores de 13 anos e com altura inferior à média são: {alunos_procurados} alunos")
        


# 2ª forma (com pandas e dicionarios):

import pandas as pd

'''Leitura da idade e altura dos alunos:
alunos = {'idade': [], 'altura': []}
for i in range(30):
    alunos['idade'].append(int(input("Idade: ")))
    alunos['altura'].append(float(input("Altura: ")))
'''

alunos = {'idade': [21,22,23,24,25,26,27,28,29,30,21,22,23,24,25,26,27,28,29,30, 21,22,23,24,25,26,27,28,29,30], 
          'altura': [1.8, 1.8, 1.7, 1.8, 1.7, 1.8, 1.7, 1.8, 1.8, 1.8, 1.8, 1.8, 1.7, 1.8, 1.7, 1.8, 1.7, 1.8, 1.8, 1.8,
                     1.8, 1.8, 1.7, 1.8, 1.7, 1.8, 1.7, 1.8, 1.8, 1.8]}


df = pd.DataFrame(alunos)

media_de_altura = df['altura'].mean()

alunos_procurados = df.loc[(df['idade'] >= 13) & (df['altura'] < media_de_altura)]

print(f"O número de alunos maiores de 13 anos e com altura inferior à média são: {len(alunos_procurados)} alunos")



        
