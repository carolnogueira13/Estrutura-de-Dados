# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

consoantes = 0
lista_de_consoantes = []
palavra = input("Digite uma palavra: ").upper()

for letra in palavra:
    if letra not in ("A", "E", "I", "O", "U"):
        consoantes += 1
        lista_de_consoantes.append(letra)

print(f"O número de consoantes da palavra são: {consoantes}")
print("E as consoantes da palavra são :", end=" ")
for c in lista_de_consoantes:
    print(c, end=" ")
        
