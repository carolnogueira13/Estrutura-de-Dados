"""Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;"""

notas = []
soma = 0
notas_acima_da_media = notas_abaixo_de_sete = 0

while True:
    nota = float(input("Insira sua nota [-1 para parar]: "))
    if nota == -1:
        break
    soma += nota
    notas.append(nota)

media = soma/len(notas)
print(f"Foram lidas {len(notas)} notas")
print("Notas na ordem que foram informadas:", end=" ")
for nota in notas:
    if nota > media:
        notas_acima_da_media += 1
    if nota < 7.0:
        notas_abaixo_de_sete += 1
    print(nota, end=" ")
print("\nNotas na ordem inversa que foram informadas:")
for nota in reversed(notas):
    print(nota) 
print(f"Soma das notas: {soma}")
print(f"Média das notas: {media:.2f}")
print(f"Quantidade de notas acima da média: {notas_acima_da_media}")
print(f"Quantidade de notas abaixo de sete: {notas_abaixo_de_sete}")
print(f"PROGRAMA ENCERRADO")


   