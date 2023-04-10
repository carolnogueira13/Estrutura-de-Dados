# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []
soma = 0
for i in range(4):
    while True:
        nota = float(input(f"Insira sua {i + 1}ª nota: "))
        if 0 <= nota <= 10:
            break
    notas.append(nota)

print("As notas informadas foram: ", end="")
for i in notas:
    print(i, end=" ")

print(f"\nA média das notas é: {sum(notas)/len(notas)}")


