# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.

alunos = 3
alunos_aprovados = 0
medias = []
for i in range(alunos):
    print("-"*30)
    notas = []
    for j in range(4):
        while True:
            nota = float(input(f"Insira sua {j + 1}ª nota do aluno {i+1}: "))
            if 0 <= nota <= 10:
                break
        notas.append(nota)
    medias.append(sum(notas)/len(notas))

print(medias)
for media in medias:
    if media >= 7.0:
        alunos_aprovados += 1

print(f"O número de alunos com média maior ou igual a sete são {alunos_aprovados}")
