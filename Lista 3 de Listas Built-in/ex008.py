# Faça um Programa que peça a idade e a altura de 5 pessoas,
# armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

pessoas = 5
dados = [[] for i in range(pessoas)]
for i in range(pessoas):
    print("-"*30)
    dados[i].append(int(input(f"Digite a idade da {i+1}ª pessoa: ")))
    dados[i].append(float(input(f"Digite a altura da {i+1}ª pessoa: ")))
print()
for i, pessoa in enumerate(dados):
    print(f"{i +1}ª pessoa: ", end="")
    pessoa.reverse()
    for j, dado in enumerate(pessoa):
        if j == 0:
            print(f"{dado} m e ", end="")
        else:
            print(f"{dado} anos")
        
        
